# kubectl client patch script

## How to

```none
if [[ -x /usr/local/bin/kubectl ]]; then
  filename="/tmp/_kubectl-completions"
  _patched_kubectl_completions="$filename-patched"

  if [ ! -e "$_patched_kubectl_completions" ]; then
    kubectl completion bash > "$filename"
    ~/Documents/python/tools/kubectl-client/completion_script_patcher.py "$filename" > "$_patched_kubectl_completions"
  fi

  source "$_patched_kubectl_completions"
  unset filename _patched_kubectl_completions
fi
```

## Results

```diff
diff --git a/tmp/_kubectl-completions b/tmp/_kubectl-completions-patched
index a556e1d..1457675 100644
--- a/tmp/_kubectl-completions
+++ b/tmp/_kubectl-completions-patched
@@ -1,19 +1,65 @@
 
-# Copyright 2016 The Kubernetes Authors.
-#
-# Licensed under the Apache License, Version 2.0 (the "License");
-# you may not use this file except in compliance with the License.
-# You may obtain a copy of the License at
-#
-#     http://www.apache.org/licenses/LICENSE-2.0
-#
-# Unless required by applicable law or agreed to in writing, software
-# distributed under the License is distributed on an "AS IS" BASIS,
-# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-# See the License for the specific language governing permissions and
-# limitations under the License.
-# bash completion for kubectl                              -*- shell-script -*-
+_kubectl_af-arbitrary-command()
+{
+    last_command="kubectl_af_arbitrary_command"
+    flags=()
+    two_word_flags=()
+    local_nonpersistent_flags=()
+    flags_with_completion=()
+    flags_completion=()
+
+    flags+=("-h")
+    flags+=("-A")
+    flags+=("-n")
+
+    two_word_flags+=("-n")
+    flags_with_completion+=("-n")
+    flags_completion+=("_watch-namespace_completions")
+}
 
+_kubectl_restart-af-services()
+{
+    last_command="kubectl_restart_af_services"
+    flags=()
+    two_word_flags=()
+    local_nonpersistent_flags=()
+    flags_with_completion=()
+    flags_completion=()
+
+    flags+=("-h")
+    flags+=("--minio")
+    flags+=("--artifactory")
+    flags+=("--no-dry-run")
+    flags+=("--no-primary")
+    flags+=("-A")
+    flags+=("-h")
+    # flags+=("-r")
+
+    two_word_flags+=("-n")
+    flags_with_completion+=("-n")
+    flags_completion+=("_watch-namespace_completions")
+
+}
+
+_kubectl_watch-namespace()
+{
+    last_command="kubectl_watch_namespace"
+    flags=()
+    two_word_flags=()
+    local_nonpersistent_flags=()
+    flags_with_completion=()
+    flags_completion=()
+
+    flags+=("-h")
+    two_word_flags+=("-r")
+    flags_with_completion+=("-r")
+    flags_completion+=("_watch-namespace_completions")
+
+    two_word_flags+=("-n")
+    flags_with_completion+=("-n")
+    flags_completion+=("_watch-namespace_completions")
+
+}
 __kubectl_debug()
 {
     if [[ -n ${BASH_COMP_DEBUG_FILE} ]]; then
@@ -50,8 +96,8 @@ __kubectl_contains_word()
     return 1
 }
 
-__kubectl_handle_go_custom_completion()
-{
+__kubectl_handle_go_custom_completion () {
+
     __kubectl_debug "${FUNCNAME[0]}: cur is ${cur}, words[*] is ${words[*]}, #words[@] is ${#words[@]}"
 
     local shellCompDirectiveError=1
@@ -79,6 +125,14 @@ __kubectl_handle_go_custom_completion()
     fi
 
     __kubectl_debug "${FUNCNAME[0]}: calling ${requestComp}"
+    if echo "$requestComp" | grep -qE -- '--namespace|-n'; then
+           __kubectl_debug '[.] Calling _watch-namespace_completions'
+           _watch-namespace_completions
+          return
+    else
+           __kubectl_debug '[.] not calling _watch-namespace_completions'
+    fi
+
     # Use eval to handle any environment variables and such
     out=$(eval "${requestComp}" 2>/dev/null)
 
@@ -12473,13 +12527,31 @@ _kubectl_wait()
     noun_aliases=()
 }
 
-_kubectl_root_command()
-{
+_kubectl_root_command () {
+
     last_command="kubectl"
 
     command_aliases=()
 
     commands=()
+    commands+=("fields")
+    commands+=("images")
+    commands+=("modify-secret")
+    commands+=("neat")
+    commands+=("rbac-lookup")
+    commands+=("sick-pods")
+    commands+=("tmux-exec")
+    commands+=("topology")
+    commands+=("view-secret")
+    commands+=("warp")
+    commands+=("who-can")
+    commands+=("get-all-resources")
+    commands+=("watch-namespace")
+    commands+=("tmux-exec")
+    commands+=("velero-annotate-all-volumes-for-pod")
+    commands+=("delete-namespace-finalizer")
+    commands+=("restart-af-services")
+    commands+=("af-arbitrary-command")
     commands+=("alpha")
     commands+=("annotate")
     commands+=("api-resources")
@@ -12635,3 +12707,4 @@ else
 fi
 
 # ex: ts=4 sw=4 et filetype=sh
+
```
