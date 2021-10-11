#!/usr/bin/env python3

import re
import sys
# import snoop

# any oc completion func
# regex = '_?_oc_.*?^}'


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
            point_in_body = 'commands=\\(\\)'
            # pre point func body -> \3
            # post point func body -> \4
            regex = '(' + func_name + '\s*\\(\\)\s*\n{((.*?' + point_in_body + ')(.*?)^)})'
            regexp = re.compile(regex, (re.M|re.DOTALL))

            replacement = func_name + ' () {\n' + \
                          '\\3' + \
                          func_body_replacement + \
                          '\\4' + \
                          '}'
        else:
            raise Exception('Point in body not true')
    else:
        replacement = func_name + ' () {\n' + \
                      func_body_replacement + \
                      '\n}'

    return (replacement, regexp)


# ('oc function name', 'if body only', 'point in body to push into')
search_params = [
                    ('_oc_root_command', True, 'commands=\\(\\)'),  # put something into a function body at a specific location
                    ('__oc_get_namespaces'),  # replace entire function
                    ('', True),  # no search parameters, prepend to completion script
                    ('', True)  # no search parameters, prepend to completion script
                ]

# replacements has to match the number of
# search parameters, indexes connect them to the
# same search-replace iteration
func_body_replacements = []
func_body_replacements.append(
        """
    commands+=("delete-namespace-finalizer")
    commands+=("get-all-namespaced-resources")
    commands+=("velero-annotate-all-volumes-for-pod")
    commands+=("watch-namespace")
    commands+=("restart-af-services")"""
)
func_body_replacements.append('    _watch-namespace_completions')
func_body_replacements.append(
    """
_oc_watch-namespace()
{
    last_command="oc_watch_namespace"
    flags=()
    two_word_flags=()
    local_nonpersistent_flags=()
    flags_with_completion=()
    flags_completion=()

    flags+=("-h")
    # flags+=("-r")
    two_word_flags+=("-r")
    flags_with_completion+=("-r")
    flags_completion+=("_watch-namespace_completions")
    # flags_completion+=("__oc_region_complete")

    two_word_flags+=("-n")
    flags_with_completion+=("-n")
    flags_completion+=("_watch-namespace_completions")

}
""")
func_body_replacements.append(
    """
_oc_restart-af-services()
{
    last_command="oc_restart_af_services"
    flags=()
    two_word_flags=()
    local_nonpersistent_flags=()
    flags_with_completion=()
    flags_completion=()

    flags+=("-h")
    flags+=("--minio")
    flags+=("--artifactory")
    flags+=("--no-dry-run")
    flags+=("-A")
    flags+=("-h")
    # flags+=("-r")

    two_word_flags+=("-n")
    flags_with_completion+=("-n")
    flags_completion+=("_restart-af-services_completions")

}
""")


# compl_script = sys.stdin.read()
with open(sys.argv[1], 'r') as f:
    compl_script = f.read()

    # remove first comment line
    compl_script = compl_script.split('\n', 2)[2]

if len(search_params) != len(func_body_replacements):
    raise Exception('Number of search parameters not equal number of replacement strings')


for index, _ in enumerate(search_params):

    func_body_replacement = func_body_replacements[index]
    start_of_file = False

    # TODO very poor design, to allow for a different number of expansion params in search_params
    try:
        func_name, body, point_in_body = search_params[index]
        replacement, regexp = get_replacement(func_name, func_body_replacement, body, point_in_body)
    except:
        try:
            _, start_of_file = search_params[index]


        except:
            func_name = search_params[index]
            replacement, regexp = get_replacement(func_name, func_body_replacement)


    # import pdb
    # pdb.set_trace()
    # print(regexp.findall(compl_script))

    if start_of_file:
        # just prepend
        compl_script = func_body_replacement + compl_script
    else:
        compl_script = regexp.sub(replacement, compl_script)

print(compl_script)
