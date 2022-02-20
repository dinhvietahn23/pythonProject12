from flask import Flask, render_template, request
import utilsfordata
import Trie

app = Flask(__name__)

root = Trie.Trie()
root.create_trie(utilsfordata.get_all_title_show())


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    SHOWS = root.auto_suggestions(request.args.get("title"))
    # SHOWS = utilsfordata.get_all_title_show()
    show = [show for show in SHOWS]
    return render_template("index.html", shows=show)


@app.route("/information")
def information():
    return render_template("information.html")


if __name__ == "__main__":
    app.run()
