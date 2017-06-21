# coding: utf-8
import pandas
from flask import Flask
from flask import Response 
import datetime
#import json
#from flask_restful import Resource, Api
#from flask_cors import CORS, cross_origin 
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

global df
df = pandas.read_csv("./test_30day.csv")
print "File loaded."

@app.route('/GetData', methods=['GET'])
def GetData():
    df["runtime"] = df["end_time"] - df["start_time"]
    means = df.groupby(["git_branch","job_name","ncpu","test_name"])["runtime"].mean()
    std = df.groupby(["git_branch","job_name","ncpu","test_name"])["runtime"].std()
    df2 = df.set_index(["git_branch","job_name","ncpu","test_name"]).join(means,how="inner",rsuffix="_mean").join(std, how="inner",rsuffix="_std")
    df2["zscore"] = (df2["runtime"] - df2["runtime_mean"])/df2["runtime_std"]
    df2 = df2.reset_index()
    df2 = df2.sort(["git_branch","job_name","ncpu","test_name","end_time"])
    ends = df2.groupby(["git_branch","job_name","ncpu","test_name"])["zscore"]
    last = ends.last().abs()
    last.sort(ascending=False)
    df3 = df2.set_index(["git_branch","job_name","ncpu","test_name"]).join(last.head(10), rsuffix="top_zscores", how="left")
    final = df3[df3["zscoretop_zscores"].notnull()]
    final = final.reset_index()
    final = final.drop(["zscoretop_zscores","runtime_std","runtime_mean"],axis=1)
    global count 
    count = 1
    def genJSON(df):
        global count
        df2 = df.set_index(["git_branch","job_name","ncpu","test_name"]) 
        jsonStr = '"' + str(count) + '"' + ':{"key":"' + " ".join([str(x) for x in df2.index[0]]) + '",'
        jsonStr += '"values":' + df2[["end_time","zscore"]].to_json(orient="records") + '}'
        count += 1
        return jsonStr
    jsonStr = final.groupby(["git_branch","job_name","ncpu","test_name"]).apply(lambda x: genJSON(x)).values
    jsonStrFinal = '{' + ",".join(jsonStr) + "}"

    return Response(jsonStrFinal, mimetype='application/json')


@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(debug=True)


