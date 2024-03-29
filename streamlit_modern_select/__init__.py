import os
import streamlit as st
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

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
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "streamlit_modern_select",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component(
        "streamlit_modern_select", path=build_dir
    )


def streamlit_modern_select(options, size=5, index=None, key=None):
    default_value = options[index] if index is not None else options[0]
    component_value = _component_func(
        options=options, size=size, index=index, key=key, default=default_value
    )
    return component_value


if not _RELEASE:
    flowers = [
        "Rose",
        "Tulip",
        "Daisy",
        "Orchid",
        "Lily",
        "Sunflower",
        "Daffodil",
        "Hyacinth",
        "Iris",
        "Peony",
    ]

    st.markdown("## Streamlit Modern Select")
    st.subheader("Options:")
    st.write(flowers)

    st.subheader("size 1, no index")
    selected_value = streamlit_modern_select(options=flowers, size=1)
    st.markdown(f"You've selected `{selected_value}`")

    st.subheader("size 6, no index")
    selected_value = streamlit_modern_select(options=flowers, size=6)
    st.markdown(f"You've selected `{selected_value}`")

    st.subheader("size 3, index 5")
    selected_value = streamlit_modern_select(options=flowers, size=3, index=5)
    st.markdown(f"You've selected `{selected_value}`")

    st.subheader("size 1, index 7")
    selected_value = streamlit_modern_select(options=flowers, size=1, index=7)
    st.markdown(f"You've selected `{selected_value}`")
