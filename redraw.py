def redraw(p_class):
    survived_chart = survived_bar_chart(df, p_class)
    title_chart = class_titles_bar_chart(df, p_class)
    hist_age = age_hist(df, p_class)
    return (
        survived_chart,
        title_chart,
        hist_age
    )