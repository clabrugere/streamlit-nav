import os
import streamlit.components.v1 as components


_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "navigation",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("navigation", path=build_dir)


def navigation(pages, default=None, key=None):
    
    if len(pages) == 0:
        raise ValueError("Must have at least one page")
    
    if default is not None and default not in pages:
        raise ValueError("Default must be a page in 'pages'")

    if not default:
        default = pages[0]

    return _component_func(
        pages=pages,
        default=default,
        key=key
    )


if not _RELEASE:
    import streamlit as st

    with st.sidebar:
        st.title("Navigation")
        pages_test = ["Page 1", "Page 2", "Page 3"]
        selected_page = navigation(pages_test)
    
    st.markdown(f"selected page: {selected_page}")
