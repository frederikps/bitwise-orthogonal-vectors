lw=('FastOrthogonalVector' 'SlowOrthogonalVector')

for i in $lw; do
	
	for j in {1..30}; do
		(( n = j * 300 ))
		for k in {1..3}; do
			echo \"$i\",$n,$(eval python gen-experiment-vectors.py $n | java $i )
		done
	done
done
