def before_feature(context, feature):
    if feature.name == 'ServiceRegistry':
        context.execute_steps('''
        Given there is an empty ServiceRegistry
        ''')
