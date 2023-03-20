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

```
colordiff < oc-completion.patch | less -R
```
