
No Conviene instalar los paquetes de python de forma general y global. Por eso usamos los ambietes virtuales


Para crear el Ambiente Virtual

mkdir graficado
cd graficado/
python3.x -m venv env

source env/bin/activate
pip install bokeh
deactivate

Bokeh
https://docs.bokeh.org/en/1.0.0/


Algunos comandos de pip:

search: busca un paquete
pip search<package>
install: instala un paquete
pip install <package>
show: muestra detalles del paquete instalado
pip show <package>
uninstall: eliminar un paquete
pip uninstall <package>
list: retorna la lista de paquetes en el ambiente actual
pip list
freeze: se utiliza para congelar los paquetes y su versión actual.
pip freeze