import streamlit as st
import time
import pandas as pd


st.set_page_config(
    page_title="Performance Optimization",
    page_icon="⚡",
)

st.title("⚡ Streamlit Performance Optimization")
st.write("Exercise 3: Performance Optimization")

st.divider()

st.subheader("1. Data Loading Performance")


@st.cache_data
def load_data():
    """Load data once and cache the result."""
    start_time = time.perf_counter()

    # Simulate a slow data-loading operation.
    time.sleep(3)

    data = pd.DataFrame(
        {
            "ID": range(1, 101),
            "Name": [f"Student {i}" for i in range(1, 101)],
            "Score": [(i * 7) % 101 for i in range(1, 101)],
        }
    )

    load_time = time.perf_counter() - start_time
    return data, load_time


start_time = time.perf_counter()

with st.spinner("Loading data..."):
    data, original_load_time = load_data()

actual_load_time = time.perf_counter() - start_time

st.success("Data loaded successfully.")

st.metric(
    "Current load time",
    f"{actual_load_time:.3f} seconds",
)

st.caption(
    f"Original data-generation time: {original_load_time:.3f} seconds"
)

st.info(
    "The first load takes longer because the data is generated. "
    "Subsequent reruns use the cached result."
)


st.divider()

st.subheader("2. Pagination")

page_size = st.selectbox(
    "Rows per page:",
    [5, 10, 20],
    index=1,
)

total_pages = (len(data) + page_size - 1) // page_size

if "page" not in st.session_state:
    st.session_state.page = 0

if st.session_state.page >= total_pages:
    st.session_state.page = total_pages - 1

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅ Previous") and st.session_state.page > 0:
        st.session_state.page -= 1

with col2:
    st.write(
        f"Page {st.session_state.page + 1} "
        f"of {total_pages}"
    )

with col3:
    if (
        st.button("Next ➡")
        and st.session_state.page < total_pages - 1
    ):
        st.session_state.page += 1


start = st.session_state.page * page_size
end = start + page_size

page_data = data.iloc[start:end]

st.dataframe(
    page_data,
    use_container_width=True,
    hide_index=True,
)

st.caption(
    f"Showing rows {start + 1}–{min(end, len(data))} "
    f"of {len(data)}"
)


st.divider()

st.subheader("3. Performance Summary")

st.markdown(
    """
### Optimizations implemented

- **`@st.cache_data`** caches the loaded data and avoids repeating the
  expensive operation on every rerun.
- **Pagination** limits the number of rows displayed at one time.
- **Loading indicator** uses `st.spinner()` while data is being loaded.
- **Performance measurement** uses `time.perf_counter()` to measure the
  data-loading operation.

### Before optimization

Without caching, the simulated 3-second data-loading operation would run
again whenever the Streamlit app reruns.

### After optimization

With `@st.cache_data`, the result is cached. Rerunning the app can reuse
the cached data instead of performing the simulated slow operation again.
"""
)