for x in 2to3 chameleon chaos crypto_pyaes deltablue django_template dulwich_log fannkuch float genshi go hexiom html5lib json_dumps json_loads logging mako meteor_contest nbody nqueens pathlib pickle pickle_dict pickle_list pickle_pure_python pidigits pyflate python_startup python_startup_no_site raytrace regex_compile regex_dna regex_effbot regex_v8 richards scimark spectral_norm sqlalchemy_declarative sqlalchemy_imperative sqlite_synth sympy telco tornado_http unpack_sequence unpickle unpickle_list unpickle_pure_python xml_etree
do
	 mkdir $x
	 cd $x
         ../../python -m pyperformance run -b $x -o $x.json
	cd ..
done

