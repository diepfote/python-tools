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
diff --git a/tmp/asdf3 b/tmp/asdf2
index a556e1d1..dad6e497 100644
--- a/tmp/asdf3
+++ b/tmp/asdf2
@@ -1,19 +1,3 @@
-
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
-
 __kubectl_debug()
 {
     if [[ -n ${BASH_COMP_DEBUG_FILE} ]]; then
@@ -12473,13 +12457,31 @@ _kubectl_wait()
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
+    commands+=("watch-namespace")
+    commands+=("tmux-exec")
+    commands+=("velero-annotate-all-volumes-for-pod")
+    commands+=("delete-namespace-finalizer")
+    commands+=("get-all-namespaced-resources")
+    commands+=("restart-af-services")
+    commands+=("af-arbitrary-command")
     commands+=("alpha")
     commands+=("annotate")
     commands+=("api-resources")
@@ -12635,3 +12637,4 @@ else
 fi
 
 # ex: ts=4 sw=4 et filetype=sh
+
```
