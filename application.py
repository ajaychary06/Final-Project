from bottle import route, post, run, template, redirect, request
import database

# Initialize the database
database.initialize_database()

@route("/")
def get_index():
    redirect("/universities")

@route("/universities")
def get_universities():
    universities = database.get_all_universities()
    return template("universities.tpl", universities=universities)

@route("/universities/add")
def get_add_university():
    return template("add_university.tpl")

@post("/universities/add")
def post_add_university():
    name = request.forms.get("name")
    location = request.forms.get("location")
    ranking = request.forms.get("ranking")
    database.add_university(name, location, ranking)
    redirect("/universities")

@route("/universities/<university_id>")
def get_university_details(university_id):
    university = database.get_university_details(university_id)
    programs = database.get_programs_for_university(university_id)
    return template("university_details.tpl", university=university, programs=programs)

@route("/universities/<university_id>/add_program")
def get_add_program(university_id):
    return template("add_program.tpl", university_id=university_id)

@post("/universities/<university_id>/add_program")
def post_add_program(university_id):
    program_name = request.forms.get("program_name")
    program_type = request.forms.get("program_type")
    database.add_program(university_id, program_name, program_type)
    redirect(f"/universities/{university_id}")

@route("/universities/<university_id>/update")
def get_update_university(university_id):
    university = database.get_university_details(university_id)
    return template("update_university.tpl", university=university)

@post("/universities/<university_id>/update")
def post_update_university(university_id):
    name = request.forms.get("name")
    location = request.forms.get("location")
    ranking = request.forms.get("ranking")
    database.update_university(university_id, name, location, ranking)
    redirect("/universities")

@route("/universities/<university_id>/delete")
def get_delete_university(university_id):
    database.delete_university(university_id)
    redirect("/universities")

run(host='localhost', port=8080)
