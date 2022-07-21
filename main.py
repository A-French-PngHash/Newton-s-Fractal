import cool_stuff

cool_stuff.points_finding_roots_images(iterations=10, points_per_unit=100, resolution=200)

graph_scale = [[-2, 2], [-2, 2]]
points_per_unit = 50
#while True:
    #cool_stuff.points_final_location_closeness_to_root(iterations=10, points_per_unit=500, resolution=400, graph_scale=graph_scale)
input("Press enter to zoom in ")
graph_scale[0][0] *= 0.9
graph_scale[0][1] *= 0.9
graph_scale[1][0] *= 0.9
graph_scale[1][1] *= 0.9
points_per_unit *= 1.23456
