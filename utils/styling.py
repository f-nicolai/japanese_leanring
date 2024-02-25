import streamlit as st


def st_write_centered(text: str, font_size: int, color: str=None, style_name: str = 'big-font'):
    style = f"""
          <style>
          .{style_name} {{
              font-size: {font_size}px !important;
              text-align: center;
      """

    if color:
        style += f"color: {color};\n"

    style += "}\n</style>"
    st.markdown(style, unsafe_allow_html=True)

    # Use the custom class in a paragraph tag to apply the styles
    st.markdown(f'<p class="{style_name}">{text}</p>', unsafe_allow_html=True)