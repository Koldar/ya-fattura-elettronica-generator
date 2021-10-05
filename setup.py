from koldar_utils.setuptools_toolbox.console_script_setup import ConsoleScriptSetup

s = ConsoleScriptSetup(
    author="Massimo Bono",
    author_mail="massimobono1@gmail.com",
    description="A utility to validate italian fatture elettroniche",
    home_page="",
    keywords=["tax","fattura-elettronica"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    main_package="fattura_elettronica_generator",
    license_name="mit",
    python_minimum_version=">=3.6",
)

if __name__ == "__main__":
    s.perform_setup()
