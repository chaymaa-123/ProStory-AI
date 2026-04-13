'use client'

import { Navigation } from '@/components/Navigation'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { ArrowRight, Sparkles, Share2, Heart, MessageCircle, Zap } from 'lucide-react'
import Link from 'next/link'

export default function Home() {
  const features = [
    {
      icon: Share2,
      title: 'Partage sans limites',
      description:
        'Partage tes expériences pro comme tu publierais sur les réseaux. C\'est facile, rapide et satisfaisant.',
    },
    {
      icon: Heart,
      title: 'Connecte-toi vraiment',
      description:
        'Découvre des histoires autentiques, des gens inspirants, et trouve ton vrai réseau professionnel.',
    },
    {
      icon: Zap,
      title: 'Crée du bruit positif',
      description:
        'Tes histoires importent. Partage tes wins, tes fails, tes apprentissages. Inspire les autres.',
    },
  ]

  const testimonials = [
    {
      quote: 'Enfin une plateforme où je peux partager mes vrais experiences sans artifices',
      author: 'Sarah M.',
      role: 'Product Manager',
    },
    {
      quote: 'Le networking n\'a jamais été aussi accessible et amusant',
      author: 'Marcus P.',
      role: 'Developer',
    },
    {
      quote: 'Je découvre des talents incroyables que je n\'aurais jamais croisés sinon',
      author: 'Lisa T.',
      role: 'Recruiter',
    },
  ]

  return (
    <main className="min-h-screen flex flex-col bg-background">
      <Navigation currentPath="/" />

      {/* Hero Section - Bold & Fun */}
      <section className="flex-1 flex items-center justify-center px-4 py-16 md:py-24">
        <div className="max-w-4xl mx-auto text-center space-y-8">
          {/* Tagline */}
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-accent/10 border border-accent/30">
            <Sparkles className="w-4 h-4 text-accent" />
            <span className="text-sm font-medium text-accent">Bienvenue sur Connex</span>
          </div>

          {/* Main Headline */}
          <div className="space-y-4">
            <h1 className="text-5xl md:text-7xl font-bold text-balance text-foreground leading-tight">
              Le networking qui fait du <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary to-accent">bruit</span>
            </h1>
            <p className="text-lg md:text-xl text-muted-foreground text-balance max-w-2xl mx-auto leading-relaxed">
              Partage tes histoires pro. Connecte-toi avec des gens vrais. Crée des opportunités. Le tout, sans prise de tête.
            </p>
          </div>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center pt-4">
            <Link href="/auth/login" className="w-full sm:w-auto">
              <Button size="lg" className="w-full rounded-xl h-12 px-8 text-base font-semibold">
                Commence maintenant
                <ArrowRight className="ml-2 w-4 h-4" />
              </Button>
            </Link>
       
          </div>

          {/* Social proof */}
          <div className="flex flex-col sm:flex-row justify-center items-center gap-6 pt-8 text-sm text-muted-foreground">
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 rounded-full bg-primary animate-pulse" />
              <span>+2,500 histoires partagées</span>
            </div>
            <div className="hidden sm:block h-5 w-px bg-border" />
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 rounded-full bg-accent animate-pulse" />
              <span>Gratuit et sans limite</span>
            </div>
            <div className="hidden sm:block h-5 w-px bg-border" />
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 rounded-full bg-primary animate-pulse" />
              <span>100% authentique</span>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section - Vibrant */}
      <section className="px-4 py-20 md:py-24 border-t border-border">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16 space-y-4">
            <h2 className="text-4xl md:text-5xl font-bold text-foreground">
              Pourquoi les gens aiment Connex
            </h2>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
              Pas de hiérarchie, pas de filtre. Juste des vrais gens, des vraies histoires.
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-6">
            {features.map((feature) => {
              const Icon = feature.icon
              return (
                <Card
                  key={feature.title}
                  className="p-8 group hover:border-primary/50 transition-all hover:shadow-lg"
                >
                  <div className="w-12 h-12 rounded-lg bg-accent/10 flex items-center justify-center group-hover:bg-accent/20 transition-colors mb-4">
                    <Icon className="w-6 h-6 text-accent" />
                  </div>
                  <h3 className="font-bold text-xl mb-3 text-foreground">
                    {feature.title}
                  </h3>
                  <p className="text-muted-foreground leading-relaxed text-sm">
                    {feature.description}
                  </p>
                </Card>
              )
            })}
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="px-4 py-20 md:py-24 bg-muted/30 border-t border-border">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-16 text-foreground">
            Ce qu\'en disent nos utilisateurs
          </h2>

          <div className="grid md:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <Card key={index} className="p-6 border-l-4 border-l-accent">
                <div className="flex gap-1 mb-4">
                  {[...Array(5)].map((_, i) => (
                    <div key={i} className="w-4 h-4 bg-accent rounded-sm" />
                  ))}
                </div>
                <blockquote className="text-muted-foreground mb-4 italic leading-relaxed">
                  "{testimonial.quote}"
                </blockquote>
                <div className="space-y-1">
                  <p className="font-semibold text-foreground text-sm">
                    {testimonial.author}
                  </p>
                  <p className="text-xs text-muted-foreground">
                    {testimonial.role}
                  </p>
                </div>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="px-4 py-20 md:py-24 border-t border-border">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-16 text-foreground">
            Comment ça marche
          </h2>

          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                step: '1',
                title: 'Crée un compte',
                description: 'C\'est hyper rapide. Deux clics et c\'est bon.',
              },
              {
                step: '2',
                title: 'Partage tes histoires',
                description: 'Tes wins, tes apprentissages, tes expériences uniques.',
              },
              {
                step: '3',
                title: 'Connecte-toi',
                description: 'Découvre d\'autres pros, échange, crée des opportunités.',
              },
            ].map((item, index) => (
              <div key={index} className="text-center space-y-4">
                <div className="w-16 h-16 rounded-full bg-primary/10 flex items-center justify-center mx-auto">
                  <span className="text-2xl font-bold text-primary">{item.step}</span>
                </div>
                <h3 className="font-bold text-lg text-foreground">{item.title}</h3>
                <p className="text-muted-foreground text-sm leading-relaxed">
                  {item.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Final CTA */}
      <section className="px-4 py-20 md:py-24 bg-primary/5 border-t border-border">
        <div className="max-w-3xl mx-auto text-center space-y-8">
          <div className="space-y-4">
            <h2 className="text-4xl md:text-5xl font-bold text-foreground">
              Prêt à faire du bruit?
            </h2>
            <p className="text-lg text-muted-foreground">
              Rejoins la communauté. Commence à partager. Tout est gratuit.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/auth/login" className="w-full sm:w-auto">
              <Button size="lg" className="w-full rounded-xl h-12 px-12 text-base font-semibold">
               Commence maintenant
                <ArrowRight className="ml-2 w-4 h-4" />
              </Button>
            </Link>
          </div>

          <p className="text-sm text-muted-foreground">
            Pas de carte de crédit requise • Tout gratuit • Zéro spam
          </p>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-border mt-auto py-8 px-4 bg-muted/20">
        <div className="max-w-6xl mx-auto">
          <div className="grid md:grid-cols-4 gap-8 mb-8">
            <div className="space-y-3">
              <h3 className="font-bold text-foreground">Connex</h3>
              <p className="text-sm text-muted-foreground">
                Le networking qui n\'est pas ennuyeux.
              </p>
            </div>
            <div className="space-y-3">
              <h4 className="font-semibold text-foreground text-sm">Produit</h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li>
                  <Link href="/feed" className="hover:text-foreground transition-colors">
                    Feed
                  </Link>
                </li>
                <li>
                  <Link href="/events" className="hover:text-foreground transition-colors">
                    Events
                  </Link>
                </li>
              </ul>
            </div>
            <div className="space-y-3">
              <h4 className="font-semibold text-foreground text-sm">Légal</h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li>
                  <Link href="#" className="hover:text-foreground transition-colors">
                    Privacy
                  </Link>
                </li>
                <li>
                  <Link href="#" className="hover:text-foreground transition-colors">
                    Terms
                  </Link>
                </li>
              </ul>
            </div>
            <div className="space-y-3">
              <h4 className="font-semibold text-foreground text-sm">Contact</h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li>
                  <Link href="mailto:hello@connex.com" className="hover:text-foreground transition-colors">
                    hello@connex.com
                  </Link>
                </li>
              </ul>
            </div>
          </div>

          <div className="border-t border-border pt-8 flex flex-col sm:flex-row justify-between items-center text-sm text-muted-foreground gap-4">
            <p>&copy; 2024 Connex. All rights reserved.</p>
            <div className="flex gap-6">
              <Link href="https://twitter.com" className="hover:text-foreground transition-colors">
                Twitter
              </Link>
              <Link href="https://linkedin.com" className="hover:text-foreground transition-colors">
                LinkedIn
              </Link>
              <Link href="https://instagram.com" className="hover:text-foreground transition-colors">
                Instagram
              </Link>
            </div>
          </div>
        </div>
      </footer>
    </main>
  )
}
