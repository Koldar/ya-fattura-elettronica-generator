from koldar_utils.setuptools_toolbox.console_script_setup import ConsoleScriptSetup

s = ConsoleScriptSetup(
    author="Massimo Bono",
    author_mail="massimobono1@gmail.com",
    description="A utility to validate italian fatture elettroniche",
    home_page="https://github.com/Koldar/ya-fattura-elettronica-generator",
    keywords=["tax", "fattura-elettronica"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    main_package="ya_fattura_elettronica_generator",
    license_name="mit",
    console_script_name="ya-fattura-elettronica-generator",
    python_minimum_version=">=3.6",
)

if __name__ == "__main__":
    s.perform_setup()
