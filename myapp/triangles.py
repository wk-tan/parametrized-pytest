# some-fail function
def triangle_type(a, b, c):
    angles = (a, b, c)
    if 90 in angles:
        return "right"
    if any([a > 90 for a in angles]):
        return "obtuse"
    if all([a < 90 for a in angles]):
        return "acute"
    if sum(angles) != 180:
        return "invalid"


# # all-pass function
# def triangle_type(a, b, c):
#     angles = (a, b, c)
#     if sum(angles) != 180 or any([a <= 0 for a in angles]):
#         return "invalid"
#     if 90 in angles:
#         return "right"
#     if any([a > 90 for a in angles]):
#         return "obtuse"
#     if all([a < 90 for a in angles]):
#         return "acute"
