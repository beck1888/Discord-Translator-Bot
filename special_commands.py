## Project info
project_state = 'alpha'
mm_dd = '1.19' # Update every time a change is made the code
days_version = 2
version_note = 'reporting_and_requesting'
# Version format (i.e. Translator Bot: alpha 1.18.2) which is mm.dd.version
version_ID = f'🛠️ Translator Bot: {project_state} {mm_dd}.{str(days_version)} #{version_note}'


## Special commands
def check_if_it_is_a_special_command(message):
    if message[0:8] == '/version':
        return version_ID
    elif message[0:5] == '/help':
        ## Get the help message and return it
        with open('help.md', 'r') as f:
            contents = f.read()
            return contents
    else:
        # No special command, and main.py knows none means to skip
        return None