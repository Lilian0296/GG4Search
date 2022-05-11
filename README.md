#  GG4Search
> ### Possible quadruplex-forming G-rich sequences finder (DNA) 
> ### Grab sequences with potential formation of quadruplexes (not for prediction)
>> ### Searching criteria: Gn1Nx1Gn2Nx2Gn3Nx3Gn4; n>=2 <see reference 1>

```python 

python GG4Search.py -i inputpath -o outputpath -c seq

# -i --input "Input-file to be analyzed. Format accepted is csv"
# -o --output "Path to output analyzed data"
# -c --column "The name of column containg DNA sequences"

```
#### This tool helps you filter DNA sequences with searching criterial, and outputs the GG counts >=4 in a csv file  
## Reference 
1. Puig Lombardi, Emilia, and Arturo Londoño-Vallejo. “A guide to computational methods for G-quadruplex prediction.” Nucleic acids research vol. 48,1 (2020): 1-15. doi:10.1093/nar/gkz1097
