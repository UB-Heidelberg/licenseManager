# -*- coding: utf-8 -*-




def index():
    grid = SQLFORM.grid(db.t_licenses,
    fields=None,
    field_id=None,
    left=None,
    headers={},
    orderby=None,
    groupby=None,
    searchable=True,
    sortable=True,
    paginate=20,
    deletable=True,
    editable=True,
    details=True,
    selectable=None,
    create=True,
    links =None,
    links_in_grid=True,
    upload='<default>',
    args=[],
    csv= False,
    user_signature=False,
    maxtextlengths={},
    maxtextlength=200,
    onvalidation=None,
    oncreate=None,
    onupdate=None,
    ondelete=None,
    sorter_icons=(XML('&#x2191;'), XML('&#x2193;')),
    ui = 'web2py',
    showbuttontext=True,
    _class="web2py_grid",
    formname='web2py_grid',
    search_widget=None,
    ignore_rw = False,
    formstyle = 'table3cols',
    exportclasses = None,
    formargs={},
    createargs={},
    editargs={},
    viewargs={},
    buttons_placement = 'left',
    links_placement = 'left')
    return locals()
