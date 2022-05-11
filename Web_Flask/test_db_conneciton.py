##Test db connection
# @app.route("/")
# def testdb():
#     try:
#         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # e is the description of the error
#         error_text = "<p>The error:<br>" + str(e) + "<p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text
