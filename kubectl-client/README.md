# kubectl client patch script

e.g. add bash completions for krew plugins

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

```
colordiff < kubectl-completion.patch | less -R
```
