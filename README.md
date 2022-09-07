All tests are designed for a screen at least with  1920x1080 resolution.

## What does this tests do?

- Main page:
  - topbar navigation
  - functionality around adding/removing to basket
  - functionality around adding/removing  to deferred list
  - functionality around adding/removing  to deferred list
  - navigation book detail, basket, deferred, compare page
- Compare page:
  - adding, removing, moving to basket, cleaning, selecting/deselecting
- Basket:
  - quantity increase/decrease
  - clear
  - restore
- Top bar: navigation
- Deferred list:
  - adding, removing, moving to basket

## Requirements 

Download and install latest geckodriver: https://github.com/mozilla/geckodriver/releases
Add geckodriver to the PATH.

## Setup:

```bash
pip install -r requirements 
```

## Run:

```bash
pytest --driver Firefox
```
