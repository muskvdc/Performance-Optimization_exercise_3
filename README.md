---
title: Streamlit Performance Optimization
emoji: ⚡
colorFrom: blue
colorTo: purple
sdk: streamlit
app_file: app.py
pinned: false
---

# Streamlit Performance Optimization

Week 4.2 — Exercise 3: Performance Optimization

This application demonstrates techniques for improving the performance
of a Streamlit application that loads data repeatedly.

## Optimizations

### 1. Data caching

The `@st.cache_data` decorator caches the result of the data-loading
function.

This prevents the simulated slow data-loading operation from running
again unnecessarily during Streamlit reruns.

### 2. Pagination

The application displays the data in pages rather than displaying all
100 rows at once.

Users can select:

- 5 rows per page
- 10 rows per page
- 20 rows per page

### 3. Loading indicator

`st.spinner()` provides visual feedback while the data-loading operation
is running.

### 4. Performance measurement

The application uses `time.perf_counter()` to measure the data-loading
operation.

The measured time is displayed in the application.

## Before vs After Performance

Performance was measured locally using `time.perf_counter()`.

| Test | Load time |
|---|---:|
| Before caching | 3.05 seconds |
| Optimized first load | 3.125 seconds |
| Optimized cached rerun | 0.004 seconds |
| Optimized page refresh | 0.002 seconds |

The first optimized load still takes approximately 3 seconds because the
cache is empty.

After the first load, `@st.cache_data` allows Streamlit to reuse the
previously loaded data instead of performing the slow data-loading
operation again.

The cached rerun completed in approximately 0.004 seconds compared with
3.05 seconds before caching, demonstrating a substantial reduction in
repeated data-loading time.

## Technologies

- Python
- Streamlit
- Pandas

## Course

Week 4.2 — Deployment

Exercise 3: Performance Optimization