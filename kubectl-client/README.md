# kubectl client patch script

## How to

```
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

```
diff --git a/tmp/_kubectl-completions b/tmp/_kubectl-completions-patched
index 4cbd4a7..320df73 100644
--- a/tmp/_kubectl-completions
+++ b/tmp/_kubectl-completions-patched
@@ -1,19 +1,46 @@
 
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
+    flags+=("-A")
+    flags+=("-h")
+    # flags+=("-r")
+
+    two_word_flags+=("-n")
+    flags_with_completion+=("-n")
+    flags_completion+=("_restart-af-services_completions")
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
 
+}
 __kubectl_debug()
 {
     if [[ -n ${BASH_COMP_DEBUG_FILE} ]]; then
@@ -13728,13 +13755,18 @@ _kubectl_wait()
     noun_aliases=()
 }
 
-_kubectl_root_command()
-{
+_kubectl_root_command () {
+
     last_command="kubectl"
 
     command_aliases=()
 
     commands=()
+    commands+=("delete-namespace-finalizer")
+    commands+=("get-all-namespaced-resources")
+    commands+=("velero-annotate-all-volumes-for-pod")
+    commands+=("watch-namespace")
+    commands+=("restart-af-services")
     commands+=("annotate")
     commands+=("api-resources")
     commands+=("api-versions")
@@ -13901,3 +13933,4 @@ else
 fi
 
 # ex: ts=4 sw=4 et filetype=sh
+
```
