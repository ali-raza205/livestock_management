from livestock_management.models import AnimalCode,AssignCode


def get_available_code():
    """Find an available code or generate a new one."""
    available_code = AnimalCode.objects.filter(code_status=False).first()
    
    if available_code:
        available_code.code_status = True  # Mark as assigned
        available_code.save()
        return available_code.code_text
    else:
        # Generate a new code if no unused codes exist
        last_code = AnimalCode.objects.order_by('-code_id').first()
        new_code = str(int(last_code.code_text) + 1) if last_code else "0001"  # Start from 1000
        return AnimalCode.objects.create(code_text=new_code, code_status=True).code_text
def assign_code_to_animal(animal):
    """Assigns an available code to a new animal."""
    animal_code = get_available_code()
    AssignCode.objects.create(animal=animal, code=AnimalCode.objects.get(code_text=animal_code))
    
def release_animal_code(animal):
    """Marks an animal's code as available when it dies or is sold."""
    assigned_code = AssignCode.objects.filter(animal=animal).first()
    
    if assigned_code:
        # Mark code as available again
        AnimalCode.objects.filter(code_id=assigned_code.code.code_id).update(code_status=False)
        assigned_code.delete()