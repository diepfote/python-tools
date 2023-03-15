#!/usr/bin/env python3

import os
import re
import subprocess
import sys
# import snoop

# any kubectl completion func
# regex = '_?_kubectl_.*?^}'

# @snoop
def get_replacement(func_name, func_body_replacement, body=False, point_in_body=''):
    # specific function name and body
    # regex = func_name + '.*?^}'

    # specific function name and body
    # submatch for whole function -> \1
    # and
    # function body -> \2
    #
    regex = '(' + func_name + '\s*\\(\\)\s*\n{(.*?^)})'
    regexp = re.compile(regex, (re.M|re.DOTALL))

    if body:
        if point_in_body:
            # pre point func body -> \4
            # post point func body -> \5
            regex = '(' + func_name + '\s*\\(\\)\s*(\\n{|{\\n)((.*?' + point_in_body + ')(.*?)^)})'
            regexp = re.compile(regex, (re.M|re.DOTALL))
            with open(f'/tmp/debug-{os.path.basename(sys.argv[0])}-kubectl.txt', 'w') as f:
                f.write(f'{regex}\n')

            replacement = func_name + ' () {\n' + \
                          '\\4' + \
                          func_body_replacement + \
                          '\\5' + \
                          '\n}'
        else:
            raise Exception('Point in body not true')
    else:
        replacement = func_name + ' () {\n' + \
                      func_body_replacement + \
                      '\n}'

    return (replacement, regexp)


search_params = []

# replacements has to match the number of
# search parameters, indexes connect them to the
# same search-replace iteration
func_body_replacements = []

# -----------------------------------------------
def format(plugin, array_name):
    return 10 * ' ' + array_name + '+=("' + plugin + '")'

kubectl_default_commands = subprocess.check_output("kubectl __completeNoDesc '' 2>/dev/null", shell=True).decode('utf-8').splitlines()[:-1]
krew_plugins = subprocess.check_output(['kubectl', 'krew', 'list']).decode('utf-8').splitlines()

kubernetes_bin_dir = os.environ['HOME'] + '/Documents/scripts/kubernetes/bin'
prefix = 'kubectl-'
kubernetes_bin_files = [bin_file.replace(prefix, '' ).replace('_', '-') \
        for bin_file in os.listdir(kubernetes_bin_dir) \
        if bin_file.startswith(prefix)]

additional_commands = ['restart-af-services', 'af-arbitrary-command']

plugin_patch = []
for plugin in kubectl_default_commands + kubernetes_bin_files + krew_plugins + additional_commands:
    plugin_patch.append(format(plugin, array_name='_all_commands'))

# ensure root command completions and namespace completions will not be overriden
search_params.append(['__kubectl_handle_completion_types', 'prepend', 'case \$COMP_TYPE in']),
func_body_replacements.append(
    '\n' +
    '        63)' +
    '\n' +
    '          return' +
    '\n' +
    '          ;;' +
    '\n'
)

# extend root commands
search_params.append(['__kubectl_get_completion_results', 'prepend', '__kubectl_debug \\"lastParam \$\{lastParam\}, lastChar \$\{lastChar\}\\"']),
func_body_replacements.append(
    '\n' +
    '    if [ ${#words[@]} -lt 3 ]; then' +
    '\n' +
    '          __kubectl_debug \'[.] Calling custom root command completions\'' +
    '\n' +
    '          _all_commands=()' +
    '\n' +
    '\n'.join(plugin_patch) +
    '\n' +
    '          COMPREPLY=()' +
    '\n' +
    '          while IFS='' read -r line; do' +
    '\n' +
    '            COMPREPLY+=("$line")' +
    '\n' +
    '          done < <(compgen -W "$(echo -e "${_all_commands[@]}")" -- "$lastParam")' +
    '\n' +
    '          __kubectl_debug "[.] compl returned ${COMPREPLY[*]}"' +
    '\n' +
    '          return' +
    '\n' +
    '    else' +
    '\n' +
    '           __kubectl_debug \'[.] not calling custom root command completions\'' +
    '\n' +
    '    fi' +
    '\n'
)

# -----------------------------------------------

# replace flag_completion function for namespaces in `_kubectl.*` functions
search_params.append(['__kubectl_get_completion_results', 'prepend', '__kubectl_debug \\"lastParam \$\{lastParam\}, lastChar \$\{lastChar\}\\"']),
func_body_replacements.append(
    '\n' +
    '    if echo "$requestComp" | grep -qE -- \'--namespace|-n\'; then' +
    '\n' +
    '           __kubectl_debug \'[.] Calling _watch-namespace_completions\'' +
    '\n' +
    '           _watch-namespace_completions' +
    '\n' +
    '          return' +
    '\n' +
    '    else' +
    '\n' +
    '           __kubectl_debug \'[.] not calling _watch-namespace_completions\'' +
    '\n' +
    '    fi' +
    '\n'
)

# -----------------------------------------------

search_params.append(['', 'prepend']),  # no search parameters, prepend to completion script
func_body_replacements.append(
    """
_kubectl_watch-namespace()
{
    last_command="kubectl_watch_namespace"
    flags=()
    two_word_flags=()
    local_nonpersistent_flags=()
    flags_with_completion=()
    flags_completion=()

    flags+=("-h")
    two_word_flags+=("-r")
    flags_with_completion+=("-r")
    flags_completion+=("_watch-namespace_completions")

    two_word_flags+=("-n")
    flags_with_completion+=("-n")
    flags_completion+=("_watch-namespace_completions")

}
""")

search_params.append(['', 'prepend']),  # no search parameters, prepend to completion script
func_body_replacements.append(
    """
_kubectl_restart-af-services()
{
    last_command="kubectl_restart_af_services"
    flags=()
    two_word_flags=()
    local_nonpersistent_flags=()
    flags_with_completion=()
    flags_completion=()

    flags+=("-h")
    flags+=("--minio")
    flags+=("--artifactory")
    flags+=("--no-dry-run")
    flags+=("--no-primary")
    flags+=("-A")
    flags+=("-h")
    # flags+=("-r")

    two_word_flags+=("-n")
    flags_with_completion+=("-n")
    flags_completion+=("_watch-namespace_completions")

}
""")

search_params.append(['', 'prepend']),  # no search parameters, prepend to completion script
func_body_replacements.append(
    """
_kubectl_af-arbitrary-command()
{
    last_command="kubectl_af_arbitrary_command"
    flags=()
    two_word_flags=()
    local_nonpersistent_flags=()
    flags_with_completion=()
    flags_completion=()

    flags+=("-h")
    flags+=("-A")
    flags+=("-n")
    flags+=("-c")

    two_word_flags+=("-n")
    flags_with_completion+=("-n")
    flags_completion+=("_watch-namespace_completions")
}
""")

search_params.append(['if \[\[ \$\(type -t compopt\) = "builtin" \]\]; then\\n\s+complete -o default -F __start_kubectl kubectl.*?fi'])
func_body_replacements.append(
    '''
if [[ $(type -t compopt) = "builtin" ]]; then
    complete -o default -F __start_kubectl k
    complete -o default -F __start_kubectl kubectl
else
    complete -o default -o nospace -F __start_kubectl k
    complete -o default -o nospace -F __start_kubectl kubectl
fi
''')

# compl_script = sys.stdin.read()
with open(sys.argv[1], 'r') as f:
    compl_script = f.read()

    # remove comment lines at start of
    # completion script
    compl_script = compl_script.split('\n', 16)[16]

    # remove vim mode line at the end
    compl_script = compl_script.rsplit('\n', 2)[0]

if len(search_params) != len(func_body_replacements):
    raise Exception('Number of search parameters not equal number of replacement strings')


for index, _ in enumerate(search_params):

    func_body_replacement = func_body_replacements[index]
    where = ''

    # TODO very poor design, to allow for a different number of expansion params in search_params
    # a, *rest = [1, 2, 3]
    # a = 1, rest = [2, 3]
    # a, *middle, c = [1, 2, 3, 4]
    # a = 1, middle = [2, 3], c = 4
    if len(search_params[index]) == 3:
        func_name, body, point_in_body = search_params[index]
        replacement, regexp = get_replacement(func_name, func_body_replacement, body, point_in_body)
    elif len(search_params[index]) == 2:
        _, where = search_params[index]
    elif len(search_params[index]) == 1:
        regex = search_params[index][0]
        replacement = func_body_replacement
        regexp = re.compile(regex, re.DOTALL)
    else:
        raise Exception('Invalid number of parameters to expand')

    # import pdb
    # pdb.set_trace()
    # print(regexp.findall(compl_script))

    if where == 'prepend':
        compl_script = func_body_replacement + compl_script
    elif where == 'append':
        compl_script = compl_script + func_body_replacement
    else:
        # if `where` is not set perform replacement
        compl_script = regexp.sub(replacement, compl_script)

print(compl_script)
