def generate_agent(name, description):
    template = f'''"""
{name}.py – {description}
"""
def run():
    print("Running {name}")
    # TODO: Implement logic here
'''
    with open(f'agents/{name}.py', 'w') as f:
        f.write(template)
