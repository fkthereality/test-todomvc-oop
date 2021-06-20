import pydantic


class Options(pydantic.BaseSettings):
    context = 'local'

    browser_name = 'chrome'
    browser_quit_after_each_test = False


_context = Options().context

options = Options(_env_file=f'tests/config.{_context}.env')
