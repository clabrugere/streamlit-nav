import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = False

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

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

    assert len(pages) > 0, "Must have at least one page"

    if not default:
        default = pages[0]

    assert default in pages, "Default must be a page name"

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
