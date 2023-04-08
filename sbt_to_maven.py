
sbt_libs="""
libraryDependencies += "org.apache.spark" % "spark-core_2.10" % "1.4.0"
libraryDependencies += "org.apache.spark" % "spark-mllib_2.10" % "1.4.0"
libraryDependencies += "org.apache.spark" % "spark-streaming_2.10" % "1.4.0"
libraryDependencies += "org.apache.spark" % "spark-streaming-kafka_2.10" % "1.4.0"
libraryDependencies += "org.mongodb" %% "casbah" % "3.0.0"
libraryDependencies += "org.jblas" % "jblas" % "1.2.4"

"""

sbt_libs=sbt_libs.split("\n")

import listUtil

sbt_libs=listUtil.remove_none(sbt_libs)

# from  strUtil.strUtil  import one_slash_to_two
import    strUtil.strUtil 
# import strUtil
# strUtil.
# import StrU 
def parse_lib(lib_str):
    # lib_str
    lib_str=strUtil.strUtil.front_del_str(lib_str,"libraryDependencies += ")
    lib_str:str 
    sps=lib_str.split(" % ")
    end_idx=-1
    groupId=sps[0]
    groupId=groupId[1:end_idx]
    artifactId=sps[1]
    artifactId=artifactId[1:end_idx]
    try:
        version=sps[2]
        version=version[1:end_idx]
        # return groupId,artifactId,version
        return f"""
        <dependency>
                <groupId>{groupId}</groupId>
                <artifactId>{artifactId}</artifactId>
                <version>{version}</version>
            </dependency>"""
    except Exception  as e:
        print("error",e)
        print("error lib_str",lib_str)

for i in  sbt_libs:
    print(parse_lib(i))
