from flask import Flask,render_template,request,redirect
from scrape.scrape_ssg import scrape_item_from_ssg
from scrape.scrape_hd import scrape_item_from_hd
from scrape.scrap_lt import scrape_item_from_lt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrap')
def scrap():
    scrap_args = request.args
    print(scrap_args)
    
    model = request.args.get("model")
    
    if bool(model) :
        ssg = request.args.get("ssg")
        hd = request.args.get("hd")
        lt = request.args.get("lt")
        if ssg != None :
            item_info = scrape_item_from_ssg(model)
        elif hd != None :
            item_info = scrape_item_from_hd(model)
        elif lt != None :
            item_info = scrape_item_from_lt(model)
        else :
            item_info = {}
    else:
        item_info = {}
        
    return render_template('item_info.html', model=model, item_info=item_info)

app.run('0.0.0.0', port=8087, debug=True)