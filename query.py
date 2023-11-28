import rdflib
g = rdflib.Graph()
g.parse("web_engineering_modules.rdf")
g.parse("Department_rdf_format.rdf")

module_list = """
SELECT DISTINCT ?moduleName ?moduleId ?deptName
WHERE {
    ?name <http://tuc.web.engineering/module#hasName> ?moduleName .
    ?id   <http://tuc.web.engineering/module#hasModuleNumber> ?moduleId .
    ?deptartment <http://tuc.web.engineering/department#hasName> ?deptName .
}"""

qres = g.query(module_list)
for row in qres:
    print(f"{row.moduleName} has id {row.moduleId} and belongs to department {row.deptName}")