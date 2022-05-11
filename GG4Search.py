import pandas as pd
import re
import io
import argparse

def get_gg_count(inpath,outpath,seq_column):
    data=pd.read_csv(inpath)
    data["gg_count"]=""
    for i in range(len(data)):
        if data.seq[i][0]=="G":
            if data.seq[i][-1]=="G" and data.seq[i][-2]=="G" and data.seq[i][-3]!="G":
                data["gg_count"][i]=len(re.split(r"G{2,}[ATCG]",data.seq[i]))
            else:
                data["gg_count"][i]=len(re.split(r"G{2,}[ATCG]",data.seq[i]))-1   
        else:
            data["gg_count"][i]=len(re.split(r"[ATCG]G{2,}",data[seq_column][i]))-1
    data=data.loc[(data["gg_count"])>=4]
    data.to_csv(outpath+"gg_search_4.csv")
    return data

parser = argparse.ArgumentParser(
    prog='python GG_4search.py',
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-i","--input",help="Input-file to be analyzed. Format accepted is csv")
parser.add_argument("-o","--output",help="Path to output analyzed data")
parser.add_argument("-c","--column",help="The name of column containg sequences")
args = parser.parse_args()

if __name__=="__main__":
    inpath = args.input
    outpath = args.output
    seq_column = args.column
    get_gg_count(inpath,outpath,seq_column)
