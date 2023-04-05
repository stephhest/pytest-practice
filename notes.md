Pytest Naming Conventions:
- Filenames: test_*.py or *_test.py
- Method names: test_*

Command Line:
- Run all tests: `pytest`
- Run tests containing a keyword: `pytest -k "method_substring"`
- Run tests in a specific file: `pytest test_file.py`
- Run tests with a specific marker: `pytest -m "marker_name"`

Running Tests in Parallel:
- Install pytest-xdist: `pip install pytest-xdist`
- Run all tests in parallel: `pytest -n 4`

Fixtures:
- Fixtures are functions that run before each test, usually to set up some data
- Fixture Methods are marked with `@pytest.fixture`, and the method name is passed as an argument to the test method that will use it
- To use a fixture method across multiple files, add it to the `conftest.py` file in the root directory

Marking Tests:
- Markers are used to group tests together
- Methods are marked with `@pytest.mark.marker_name`
- Custom markers can be added to `pytest.ini` file

Skipping Tests:
- Tests can be skipped by adding `@pytest.mark.skip` to the method
- Test failures can be ignored by adding `@pytest.mark.xfail` to the method

Test Reporting:
- Install pytest-html: `pip install pytest-html`
- Run tests with html report: `pytest --html=report.html`
- Create a results XML file: `pytest <optional_filen> -v --junitxml=results.xml`


