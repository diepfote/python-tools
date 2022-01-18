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
diff --git a/tmp/_oc-completions b/tmp/_oc-completions-patched
index 9c7d488..cff4595 100644
--- a/tmp/_oc-completions
+++ b/tmp/_oc-completions-patched
@@ -1,5 +1,47 @@
 
-# bash completion for oc                                   -*- shell-script -*-
+_oc_restart-af-services()
+{
+    last_command="oc_restart_af_services"
+    flags=()
+    two_word_flags=()
+    local_nonpersistent_flags=()
+    flags_with_completion=()
+    flags_completion=()
+
+    flags+=("-h")
+    flags+=("--minio")
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
+_oc_watch-namespace()
+{
+    last_command="oc_watch_namespace"
+    flags=()
+    two_word_flags=()
+    local_nonpersistent_flags=()
+    flags_with_completion=()
+    flags_completion=()
+
+    flags+=("-h")
+    # flags+=("-r")
+    two_word_flags+=("-r")
+    flags_with_completion+=("-r")
+    flags_completion+=("_watch-namespace_completions")
+    # flags_completion+=("__oc_region_complete")
+
+    two_word_flags+=("-n")
+    flags_with_completion+=("-n")
+    flags_completion+=("_watch-namespace_completions")
+
+}
 
 __oc_debug()
 {
@@ -297,13 +339,8 @@ __oc_parse_get()
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
@@ -20474,13 +20511,18 @@ _oc_whoami()
     noun_aliases=()
 }
 
-_oc_root_command()
-{
+_oc_root_command () {
+
     last_command="oc"
 
     command_aliases=()
 
     commands=()
+    commands+=("delete-namespace-finalizer")
+    commands+=("get-all-namespaced-resources")
+    commands+=("velero-annotate-all-volumes-for-pod")
+    commands+=("watch-namespace")
+    commands+=("restart-af-services")
     commands+=("adm")
     commands+=("annotate")
     commands+=("api-resources")
@@ -20637,3 +20679,4 @@ else
 fi
 
 # ex: ts=4 sw=4 et filetype=sh
+
```
