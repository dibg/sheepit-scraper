@app.route("/v1/block")
def block():
    username_to_block = request.args.get('username')
    if not username_to_block:
        return "username is not provided"
    block_user(get_valid_login_session(), username_to_block)
    return "User " + username_to_block + " is blocked"


@app.route("/v1/raw_data")
def raw_data():
    data = retrieve_json("data")
    return jsonify(data)


@app.route("/v1/load_stored_data_to_db")
def load_data():
    json_data = load_or_if_not_exits_create_json_file("data")
    for entry in json_data:
        data = Data(entry)
        insert_data(data)
    return "ok"


@app.route("/v1/db_create")
def create_db():
    db.create_all()
    return "ok"


@app.route("/v1/db_delete")
def delete_db():
    Data.query.delete()
    db.session.commit()
    return "ok"