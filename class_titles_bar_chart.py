def class_titles_bar_chart(dataset, pass_class, cpalette=palette):
    ttl_data = dataset[dataset['Pclass'] == int(pass_class)]
    title_possibilities = list(ttl_data['Title'].value_counts().index)
    title_values = list(ttl_data['Title'].value_counts().values)
    int_possibilities = np.arange(len(title_possibilities))
    
    source = ColumnDataSource(data={
        'titles': title_possibilities,
        'titles_int': int_possibilities,
        'values': title_values
    })

    hover_tool = HoverTool(
        tooltips=[('Title', '@titles'), ('Count', '@values')]
    )
    
    chart_labels = {}
    for val1, val2 in zip(source.data['titles_int'], source.data['titles']):
        chart_labels.update({ int(val1): str(val2) })
        
    p = figure(tools=[hover_tool], plot_height=300, title='Titles for Current Class')
    p.vbar(x='titles_int', top='values', source=source, width=0.9,
           fill_color=factor_cmap('titles', palette=palette_generator(len(source.data['titles']), cpalette), factors=source.data['titles']))
    
    plot_styler(p)
    p.xaxis.ticker = source.data['titles_int']
    p.xaxis.major_label_overrides = chart_labels
    p.xaxis.major_label_orientation = math.pi / 4
    p.sizing_mode = 'scale_width'
    
    return p