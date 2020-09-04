def survived_bar_chart(dataset, pass_class, cpalette=palette[1:3]):
    surv_data = dataset[dataset['Pclass'] == int(pass_class)]
    surv_possibilities = list(surv_data['Survived'].value_counts().index)
    surv_values = list(surv_data['Survived'].value_counts().values)
    surv_possibilities_text = ['Did not Survive', 'Survived']
        
    source = ColumnDataSource(data={
        'possibilities': surv_possibilities,
        'possibilities_txt': surv_possibilities_text,
        'values': surv_values
    })

    hover_tool = HoverTool(
        tooltips=[('Survived?', '@possibilities_txt'), ('Count', '@values')]
    )
    
    p = figure(tools=[hover_tool], plot_height=400, title='Did/Did not Survive for Current Class')
    p.vbar(x='possibilities', top='values', source=source, width=0.9,
           fill_color=factor_cmap('possibilities_txt', palette=palette_generator(len(source.data['possibilities_txt']), cpalette), factors=source.data['possibilities_txt']))
    
    plot_styler(p)
    p.xaxis.ticker = source.data['possibilities']
    p.xaxis.major_label_overrides = { 0: 'Did not Survive', 1: 'Survived' }
    p.sizing_mode = 'scale_width'
    
    return p