
for x in 2to3 chameleon chaos crypto_pyaes deltablue django_template dulwich_log fannkuch float genshi go hexiom html5lib json_dumps json_loads logging mako meteor_contest nbody nqueens pathlib pickle pick
do
         echo $x
         cd $x
         python3 ../../postProcessing.py
        cd ..
done

