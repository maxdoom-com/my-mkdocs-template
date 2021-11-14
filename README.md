My mkdocs template
==============================================================================



Installation
------------------------------------------------------------------------------

```sh
python3 -m venv env
env/bin/pip install -r requirements.txt
env/bin/pip install --editable custom_fences # if you want to use the custom_fences
```

If you don't want to use custom fences disable this config part in the
`mkdocs.yml` config file:

```yaml
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - { name: plain, class: plain, format: !!python/name:custom_fences.plain }

```


Building the HTML
------------------------------------------------------------------------------

```sh
./build-docs.sh
```


Building the SVGs
------------------------------------------------------------------------------

```sh
./build-svgs.sh
```


Running the development server
------------------------------------------------------------------------------

```sh
./run.sh
```
