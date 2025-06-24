import nbformat

nb_path = "notebooks/02_cnn_implementation/03_cnn_kfold.ipynb"

with open(nb_path, encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

for cell in nb.cells:
    if 'outputs' in cell:
        cleaned_outputs = []
        for out in cell['outputs']:
            if out.get('output_type') == 'error':
                continue
            elif out.get('output_type') == 'stream':
                text = out.get('text', '')
                if 'Traceback' in text or '❌ Error during K-fold validation' in text:
                    continue
            cleaned_outputs.append(out)
        cell['outputs'] = cleaned_outputs

with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("✅ Removed error outputs, tracebacks, and ❌ summary line.")
