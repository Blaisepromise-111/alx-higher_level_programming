0x07. Python - Test-driven development

The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.

To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.

To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.

doctest tests source code by running examples embedded in the documentation and verifying that they produce the expected results. It works by parsing the help text to find examples, running them, then comparing the output text against the expected value.
