pyinstaller IntelPy.py --noconsole --onefile --add-data intelpy\resources;intelpy\resources --noconfirm --icon=intelpy\gui\goodpie2.ico
copy -R intelpy/resources dist/