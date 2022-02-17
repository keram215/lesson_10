from flask import Flask
import utils

app = Flask(__name__)

@app.route('/',)
def page_index():
    candidates = utils.get_candidates_all()
    page_content = utils.build_performatted_list(candidates)
    return  page_content

@app.route(("/skill/<skill_name>"))
def page_skill(skill_name):

    candidates = utils.get_candidates_by_skill(skill_name)

    page_content = utils.build_performatted_list(candidates)
    return page_content

@app.route("/candidate/<int:vid>")

def page_candidate(vid):

    candidate = utils.get_candidate_by_id(vid)

    page_content = f"<pre>"
    page_content += f"{candidate['name']} \n"
    page_content += f"{candidate['position']} \n"
    page_content += f"{ candidate['skills']} \n"
    page_content += f"</pre>"

    return page_content


    return page_content
app.run()