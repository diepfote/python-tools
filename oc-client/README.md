# oc client patch script

## How to

```none
if [[ -x /usr/local/bin/oc ]]; then
  filename="/tmp/_oc-completions"
  _patched_oc_completions="$filename-patched"

  if [ ! -e "$_patched_oc_completions" ]; then
    oc completion bash > "$filename"
    ~/Documents/python/tools/oc-client/completion_script_patcher.py "$filename" > "$_patched_oc_completions"
  fi

  source "$_patched_oc_completions"
  unset filename _patched_oc_completions
fi
```

## Results

```diff
diff --git a/tmp/asdf b/tmp/asdf1
index 9c7d4881..1735a26b 100644
--- a/tmp/asdf
+++ b/tmp/asdf1
@@ -1,6 +1,4 @@
 
-# bash completion for oc                                   -*- shell-script -*-
-
 __oc_debug()
 {
     if [[ -n ${BASH_COMP_DEBUG_FILE} ]]; then
@@ -297,13 +295,8 @@ __oc_parse_get()
     fi
 }
 
-__oc_get_namespaces()
-{
-    local template oc_out
-    template="{{ range .items  }}{{ .metadata.name }} {{ end }}"
-    if oc_out=$(oc get -o template --template="${template}" namespace 2>/dev/null); then
-        COMPREPLY=( $( compgen -W "${oc_out[*]}" -- "$cur" ) )
-    fi
+__oc_get_namespaces () {
+    _watch-namespace_completions
 }
 
 __oc_get_resource()
@@ -20474,13 +20467,31 @@ _oc_whoami()
     noun_aliases=()
 }
 
-_oc_root_command()
-{
+_oc_root_command () {
+
     last_command="oc"
 
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
     commands+=("adm")
     commands+=("annotate")
     commands+=("api-resources")
@@ -20637,3 +20648,4 @@ else
 fi
 
 # ex: ts=4 sw=4 et filetype=sh
+
```
