#! /bin/bash

# Paul Aguilar (penserbjorne)
# Elimina los archivos viejos y construye el sitio

echo "Eliminando archivos."
rm -rf author category drafts tag theme *.html

echo "Construyendo el sitio."
cd pelican
pelican content -o ..

echo "Mostrando el sitio."
pelican --listen -o ..
