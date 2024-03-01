import streamlit as st
from pandas import read_csv, DataFrame, concat
from pathlib import Path
from typing import Union


def render_config_tab():
    with st.sidebar:
        st.header("Configuration")
        st.write("Select units you want ot include")
        for section_number, unit_numbers in st.session_state.config.items():
            with st.expander(f'Section {section_number}:'):
                st.checkbox(
                    'All',
                    key=f'config.{section_number}_all',
                    value=st.session_state.checkbox_all[section_number],
                    on_change=select_all_units_from_section,
                    kwargs={'section': section_number}
                )
                for unit_number in unit_numbers:
                    st.checkbox(
                        f"Unit {unit_number}",
                        key=f"config.{section_number}_{unit_number}",
                        value=st.session_state.checkbox_values[section_number][unit_number],
                        on_change=update_config_filters,
                        kwargs={'checkbox_id': f"config.{section_number}_{unit_number}"}
                    )

        st.radio("Language", ["English", "French"], key="config.language")
        st.checkbox('Shuffle without replacement ?', key='config.random', value=True)
        # st.number_input('# of samples', value=10000, format="%d", key='config.n_samples')


def select_all_units_from_section(section: str):
    st.session_state.filters[section] = st.session_state.config[section].copy()
    if st.session_state[f'config.{section}_all']:
        for unit in st.session_state.checkbox_values[section].keys():
            st.session_state.checkbox_values[section][unit] = True
            add_unit_from_without_replacement_dataframe(section=int(section), unit=int(unit))

    else:
        for x in range(len(st.session_state.checkbox_values[section])):
            for unit in st.session_state.checkbox_values[section].keys():
                st.session_state.checkbox_values[section][unit] = False
                remove_unit_from_without_replacement_dataframe(section=int(section), unit=int(unit))


def update_config_filters(checkbox_id: str):
    section, unit = checkbox_id.replace('config.', '').split('_')
    if st.session_state[checkbox_id]:
        st.session_state.filters[int(section)].append(int(unit))
        add_unit_from_without_replacement_dataframe(section=int(section), unit=int(unit))
    else:
        st.session_state.filters[int(section)].remove(int(unit))
        st.session_state.checkbox_all[int(section)] = False
        remove_unit_from_without_replacement_dataframe(section=int(section), unit=int(unit))


@st.cache_data
def load_data() -> (DataFrame, DataFrame, DataFrame):
    return read_csv(Path(__file__).parent.parent / 'data/verbs.csv', sep=';'), read_csv(
        Path(__file__).parent.parent / 'data/words.csv', sep=';'), read_csv(
        Path(__file__).parent.parent / 'data/counters.csv', sep=';')


def initialize_internal_config():
    st.session_state.verbs, st.session_state.kanjis, st.session_state.counters = load_data()

    config: dict[str, list[Union[int, list[int]]]] = st.session_state.kanjis[['section', 'unit']]\
        .sort_values(['section', 'unit'],ascending=[0,0]) \
        .drop_duplicates() \
        .groupby('section', as_index=False) \
        .agg(units=('unit', list)) \
        .to_dict('list')

    st.session_state.config: dict[int, list[int]] = dict(zip(config['section'], config['units']))
    st.session_state.filters: dict[int, list[int]] = {x: [] for x in config['section']}
    st.session_state.checkbox_values: dict[int, dict[int, bool]] = {x: {y: False for y in st.session_state.config[x]}
                                                                    for x in config['section']}
    st.session_state.checkbox_all: dict[int, bool] = {x: False for x in config['section']}
    st.session_state['kanji_quizz.current_state'] = 'original'
    st.session_state.kanji_sample_without_replacement = DataFrame()
    st.session_state.verbs_sample_without_replacement = DataFrame()


def get_dataframe_filter(resource: str):
    if resource == 'words':
        filter = st.session_state.kanjis
    elif resource == 'verbs':
        filter = st.session_state.verbs

    filter = (st.session_state.kanjis['section'].isnull())
    for section, units in st.session_state.filters.items():
        filter = filter | (
                (st.session_state.kanjis['section'] == section)
                & st.session_state.kanjis['unit'].isin(units)
        )
    return filter


def initialize_without_replacement_dataframe(resource: str) -> DataFrame:
    if resource == 'words':
        return st.session_state.kanjis.loc[get_dataframe_filter(resource=resource)]

    elif resource == 'verbs':
        return st.session_state.verbs.loc[get_dataframe_filter(resource=resource)]


def add_unit_from_without_replacement_dataframe(section: int, unit: int):
    st.session_state.kanji_sample_without_replacement = concat([
        st.session_state.kanji_sample_without_replacement,
        st.session_state.kanjis.loc[
            (st.session_state.kanjis['section'] == section)
            & (st.session_state.kanjis['unit'] == unit)]
    ]).sample(frac = 1)

    st.session_state.verbs_sample_without_replacement = concat([
        st.session_state.verbs_sample_without_replacement,
        st.session_state.verbs.loc[
            (st.session_state.kanjis['section'] == section)
            & (st.session_state.kanjis['unit'] == unit)]
    ]).sample(frac = 1)


def remove_unit_from_without_replacement_dataframe(section: int, unit: int):
    st.session_state.kanji_sample_without_replacement = \
        st.session_state.kanji_sample_without_replacement.drop(
            st.session_state.kanjis.loc[
                (st.session_state.kanjis['section'] == section)
                & (st.session_state.kanjis['unit'] == unit)].index
        ).sample(frac = 1)

    st.session_state.verbs_sample_without_replacement = \
        st.session_state.verbs_sample_without_replacement.drop(
            st.session_state.verbs.loc[
                (st.session_state.kanjis['section'] == section)
                & (st.session_state.kanjis['unit'] == unit)].index
        ).sample(frac = 1)
