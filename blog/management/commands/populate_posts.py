from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args: Any, **options: Any):
        Post.objects.all().delete()
        
        titles =[
    "Exploring the Beauty of Nature",
    "The Power of Positive Thinking",
    "10 Tips to Improve Your Coding Skills",
    "Secrets of a Productive Morning Routine",
    "How to Build Confidence and Self-Esteem",
    "The Future of Artificial Intelligence",
    "Simple Recipes for Busy People",
    "How to Start a Career in Tech",
    "Benefits of Daily Meditation",
    "Travel Guide: Hidden Gems of India",
    "Mastering Time Management",
    "Why Reading Books Changes Your Life",
    "Best Free Tools for Developers",
    "How to Stay Motivated During Hard Times",
    "The Rise of Sustainable Fashion",
    "How to Create a Personal Portfolio Website",
    "Photography Tips for Beginners",
    "Understanding Mental Health Awareness",
    "Learn Python in 30 Days",
    "Exploring Space: The Next Frontier",
]

        contents =[
          "Nature has an incredible way of healing our hearts and calming our minds. The sound of birds, the rustling of leaves, and the sight of mountains remind us that peace still exists beyond screens and schedules.Spending time in nature not only reduces stress but also increases creativity and mental clarity. The more we connect with the natural world, the more balanced and joyful our lives become.",
          "Positive thinking is not ignoring your problems — it’s facing them with hope and strength. When you train your mind to see possibilities instead of obstacles, your attitude transforms your outcomes.A simple shift in mindset can change how you react to challenges. Start each morning with gratitude and affirmations, and you’ll begin to notice more good things happening around you.",
          "Becoming a better coder isn’t about memorizing syntax — it’s about solving problems. Practice daily, break big tasks into smaller parts, and read other people’s code.Join coding communities, ask questions, and never stop learning new concepts. The more you build, the better you become.",
          "A productive morning doesn’t mean rushing through your to-do list. It’s about setting your mind and energy in the right direction.Wake up early, drink water, and spend a few minutes planning your day. When you start slow and intentional, the rest of your day flows smoothly.",
          "Confidence grows every time you keep a promise to yourself. When you finish tasks you said you would, your self-esteem naturally rises.Surround yourself with people who encourage you and avoid comparing your progress with others. Believe in your journey — confidence is built step by step.",
          "Artificial Intelligence is changing the way we live, work, and think. It helps automate daily tasks, improve decision-making, and create smarter systems.But with great power comes great responsibility — AI should be developed with fairness, safety, and ethics in mind to truly benefit humanity.",
          "Cooking doesn’t need to be complicated. A few fresh ingredients and simple recipes can make your meals healthy and quick.Try one-pan dishes, salads, and smoothies. Preparing your food gives you control over what you eat — a small step toward a better lifestyle.",
          "Starting a career in tech might look hard, but everyone begins somewhere. Learn one skill at a time — start with HTML, Python, or JavaScript.Build small projects and showcase them in your portfolio. What matters most is curiosity and persistence, not perfection.",
          "Meditation brings silence to the chaos inside us. Even 10 minutes of deep breathing can help you focus better and feel lighter.With regular practice, meditation reduces stress, improves mood, and teaches emotional balance. It’s the most peaceful way to recharge your mind.",
          "India is filled with beautiful destinations that most people overlook — hidden waterfalls, peaceful beaches, and quiet hill stations.Exploring lesser-known places helps you experience real culture and connect with locals. Every trip teaches you something new about life and simplicity.",
          "Time management is the difference between being busy and being effective. Learn to prioritize — not everything deserves your time.Break your goals into smaller parts, use reminders, and rest when needed. Managing your time means managing your energy wisely.",
          "Reading books is like having a conversation with the greatest minds in history. Every page teaches something new — a story, a perspective, or a truth.When you make reading a habit, you develop patience, focus, and empathy. A good book can truly change your life.",
          "There are amazing free tools available for developers today — code editors, design kits, and testing platforms.Use tools like VS Code, GitHub, and Figma to make your projects faster and cleaner. The right tools save time and boost creativity.",
          "Motivation is not constant — it comes and goes. That’s why discipline matters more.When you feel tired, take small steps instead of quitting. Every little effort adds up, and consistency always beats intensity.",
          "Sustainable fashion is all about protecting our planet through smart choices. Buying less but better, recycling clothes, and supporting ethical brands make a big difference.It’s not just a trend — it’s a movement toward a cleaner, fairer world.",
          "A personal portfolio website is your online identity. It shows your skills, creativity, and projects to employers or clients.Keep the design simple, highlight your best work, and update it regularly. Your website speaks before you do — make it count.",
          "Photography is about emotion, not equipment. Light, timing, and composition create magic more than an expensive camera.Try capturing daily life from new angles — moments, smiles, and shadows. The world looks different when you learn to see through a lens.",
          "Mental health matters more than people realize. It affects how we think, act, and relate to others.Talking about emotions, taking breaks, and seeking help when needed can heal more than silence ever could. Be kind — everyone is fighting a battle you can’t see.",
          "Python is one of the easiest languages to learn, but it’s also extremely powerful. Start with the basics — loops, functions, and data types.Once you’re comfortable, try making small apps or games. The key is to practice daily and enjoy the process.",
          "Space exploration reminds us how tiny yet powerful humanity can be. Every new discovery about planets or galaxies expands our curiosity.It inspires scientists, artists, and dreamers to think beyond what’s visible — a beautiful reminder that our journey has just begun.",
    ]

        img_url =[
        "https://picsum.photos/id/1/800/400",
        "https://picsum.photos/id/2/800/400",
        "https://picsum.photos/id/3/800/400",
        "https://picsum.photos/id/4/800/400",
        "https://picsum.photos/id/5/800/400",
        "https://picsum.photos/id/6/800/400",
        "https://picsum.photos/id/7/800/400",
        "https://picsum.photos/id/8/800/400",
        "https://picsum.photos/id/9/800/400",
        "https://picsum.photos/id/10/800/400",
        "https://picsum.photos/id/11/800/400",
        "https://picsum.photos/id/12/800/400",
        "https://picsum.photos/id/13/800/400",
        "https://picsum.photos/id/14/800/400",
        "https://picsum.photos/id/15/800/400",
        "https://picsum.photos/id/16/800/400",
        "https://picsum.photos/id/17/800/400",
        "https://picsum.photos/id/18/800/400",
        "https://picsum.photos/id/19/800/400",
        "https://picsum.photos/id/20/800/400",
        
    ]        
        
        categories = Category.objects.all()
        for title, content, img_url in zip(titles,contents,img_url):
            category = random.choice(categories)
            Post.objects.create(title=title,content=content,img_url=img_url,category=category)

        self.stdout.write(self.style.SUCCESS("Completed Inserting Data!"))