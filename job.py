class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    # Step 1: Sort jobs by descending profit
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    max_deadline = max(job.deadline for job in jobs)
    
    # Initialize time slots to None (no job assigned)
    slots = [None] * max_deadline
    
    total_profit = 0
    scheduled_jobs = []
    
    # Step 2: Schedule jobs greedily
    for job in jobs:
        # Find a free slot for this job before its deadline (starting from the last possible slot)
        for slot in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = job.job_id
                total_profit += job.profit
                scheduled_jobs.append(job.job_id)
                break
                
    return scheduled_jobs, total_profit

# Example usage
jobs_list = [
    Job('J1', 2, 100),
    Job('J2', 1, 19),
    Job('J3', 2, 27),
    Job('J4', 1, 25),
    Job('J5', 3, 15)
]

scheduled, profit = job_scheduling(jobs_list)
print("Scheduled Jobs:", scheduled)
print("Total Profit:", profit)
